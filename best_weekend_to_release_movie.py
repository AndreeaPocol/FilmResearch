import json
import adjust_revenue_for_inflation as arfi
from re import sub
from collections import defaultdict
import numpy as np
import csv


fileNames = ["first_omdb_movies.json", "second_omdb_movies.json"]
filter = False # filter out movies less than 75 minutes long
includeAllCountries = True
releasedInCountryOfInterest = []
genresToConsider = {
    "Horror": [],
    "Romance": [],
    "Comedy": [],
    "Action": [],
    "Adventure": [],
    "Animation": [],
    "Crime": [],
    "Drama": [],
}
write = True # write data to a CSV

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
        if genre in genresToConsider.keys():
            movie = { "ReleaseDate": releaseDate, "Revenue": revenue}
            genresToConsider[genre].append(movie)


def presentResults(revenueByReleaseWeek, genre):
    filename = (
            "release_week_vs_box_office_revenue_{genre}_genre".format(
                genre=genre.lower()
            )
        )

    if write:
        header = ["Release Week", "Box Office Revenue"]
        with open(filename + ".csv", 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)
            for releaseWeek, revenues in revenueByReleaseWeek.items():
                writer.writerow([releaseWeek, np.average(revenues)])

        # with open(filename + ".csv", "w+") as csvfile:
        #     filewriter = csv.writer(csvfile, delimiter=",")
        #     filewriter.writerow(header)
        #     filewriter.writerows(points)


def releaseWeekVsRevenue():
    # releaseWeeks = []
    # revenues = []
    numMovies = 0
    totalMovies = 0
    revenueByReleaseWeek = defaultdict(list)

    for fileName in fileNames:
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
            if filter:
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
            if not includeAllCountries:
                if not releasedInCountryOfInterest(countries):
                    continue
            revenue = float(sub(r"[^\d.]", "", boxOffice))
            revenue = arfi.adjustRevenueForInflation(revenue, releaseYear)
            releaseDate = releaseDate.split(' ')
            # revenues.append(revenue)
            # releaseWeeks.append(getWeek(int(releaseDate[0]), releaseDate[1]))
            week = getWeek(int(releaseDate[0]), releaseDate[1])
            revenueByReleaseWeek[week].append(revenue)
            # addMoviesToGenreLists(releaseDate, revenue, movieGenres)

            numMovies += 1
    print("Processed {numMovies} movies of {totalMovies} total movies".format(numMovies=numMovies, totalMovies=totalMovies))
    # print(f"releaseWeeks: {releaseWeeks}")
    # print(f"revenues: {revenues}")
    presentResults(revenueByReleaseWeek, "all")


def main():
    releaseWeekVsRevenue()


if __name__ == "__main__":
    main()