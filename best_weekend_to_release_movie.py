import json
import adjust_revenue_for_inflation as arfi
from re import sub
from collections import defaultdict
import numpy as np
import csv
import constants as c


def getWeek(date, month):
    week = ""
    if 1 <= date and date <= 7:
        week = "Week 1"
    elif 8 <= date and date <= 14:
        week = "Week 2"
    elif 15 <= date and date <= 21:
        week = "Week 3"
    elif 22 <= date and date <= 28:
        week = "Week 4"
    elif 28 <= date:
        week = "Week 5"
    return " ".join([month, week])
        

def addMoviesToGenreLists(releaseDate, revenue, movieGenres):
    for genre in movieGenres:
        if genre in c.genresToConsider.keys():
            movie = { "ReleaseDate": releaseDate, "Revenue": revenue}
            c.genresToConsider[genre].append(movie)


def releaseWeekVsRevenueByGenre():
    filename = "release_week_vs_box_office_revenue_by_genre"
    if c.write:
        header = ["Genre", "Release Month", "Release Week", "Box Office Revenue"]
        with open(filename + ".csv", 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)

    for genre in c.genresToConsider.keys():
        revenueByReleaseWeekAndGenre = defaultdict(list)
        movies = c.genresToConsider[genre]
        for movie in movies:
            releaseWeek = movie["ReleaseDate"]
            revenue = movie["Revenue"]
            revenueByReleaseWeekAndGenre[releaseWeek].append(revenue)
        print(
            "Finished processing {numMovies} {genre} movies".format(
                numMovies=len(movies), genre=genre
            )
        )

        with open(filename + ".csv", 'a') as csv_file:
            writer = csv.writer(csv_file)
            for releaseWeek, revenues in revenueByReleaseWeekAndGenre.items():
                writer.writerow([releaseWeek.split(' ')[0], releaseWeek, np.average(revenues), genre])


def releaseWeekVsRevenue():
    numMovies = 0
    totalMovies = 0
    revenueByReleaseWeek = defaultdict(list)

    for fileName in c.fileNames:
        with open(fileName) as f:
            movies = json.load(f)
        for movie in movies.items():
            movie = movie[1]
            totalMovies += 1
            if (
                "BoxOffice" not in movie
                or "Country" not in movie
                or "Released" not in movie
                or "Type" not in movie
                or "Genre" not in movie
            ):
                continue
            if c.filter:
                if (
                    "Runtime" not in movie 
                    or movie["Runtime"] == "N/A" 
                    or int(movie["Runtime"].split(" ")[0]) < 75.0
                ):
                    continue
            countries = movie["Country"].split(",")
            boxOffice = movie["BoxOffice"]
            type = movie["Type"]
            releaseDate = movie["Released"]
            releaseYear = movie["Year"]
            movieGenres = movie["Genre"].split(",")
            if (
                boxOffice == "N/A" 
                or releaseDate == "N/A"
                or  type != "movie"
            ):
                continue
            if not c.includeAllCountries:
                if not c.releasedInCountryOfInterest(countries):
                    continue
            revenue = float(sub(r"[^\d.]", "", boxOffice))
            revenue = arfi.adjustRevenueForInflation(revenue, releaseYear)
            releaseDate = releaseDate.split(' ')
            week = getWeek(int(releaseDate[0]), releaseDate[1])
            revenueByReleaseWeek[week].append(revenue)
            addMoviesToGenreLists(week, revenue, movieGenres)
            numMovies += 1
    print("Processed {numMovies} movies of {totalMovies} total movies".format(numMovies=numMovies, totalMovies=totalMovies))
    

    filename = "release_week_vs_box_office_revenue_all_genres"
    if c.write:
        header = ["Release Month", "Release Week", "Box Office Revenue"]
        with open(filename + ".csv", 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)
            for releaseWeek, revenues in revenueByReleaseWeek.items():
                writer.writerow([releaseWeek.split(' ')[0], releaseWeek, np.average(revenues)])



def main():
    releaseWeekVsRevenue()
    # releaseWeekVsRevenueByGenre()


if __name__ == "__main__":
    main()