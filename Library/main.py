def modernfilms_with_a_large_number_of_ratings(movies,rating_count):
    """
    Данная функция показывает фильмы выпущенные после 2006 года с количеством оценок больше 100.
    •	movies: таблица со всеми фильмами
    •	rating_count: таблица с количеством отзывов
    """
    # new_movies=movies[movies["year"]>2006]
    # rating_count_100 = rating_count[rating_count["rating"]>100]
    # new_movies_100=rating_count_100.merge(new_movies, how = 'inner', left_on='movieId', right_on='movieId')


def comedies_with_ratings_from_all_users(comedy, rating):
    """
    Данная функция показывает рейтинг от каждого пользователя к фильмам жанра комедия.
    •	comedy: таблица с фильмами только определенного жанра
    •	 rating: таблица с рейтингами от пользователей
    """
    # comedy_all_rating = rating.merge(comedy)
    # del comedy_all_rating['year']
    # del comedy_all_rating['userId']


def new_items_rated_5_5(movies, rating_max):
    """
    Данная функция показывает новые фильмы, которые хотя бы один пользователь оценил на 5.5.
    •	movies: таблица со всеми фильмами
    •     rating_max: таблица с максимальными рейтингами
    """
    # supernew_movies=movies[movies["year"]>=2017]
    # rating_max_5_5 = rating_max[rating_max["rating"]==5.5]
    # supernew_movies_5_5=rating_max_5_5.merge(supernew_movies, left_on='movieId', right_on='movieId')


def сomedies_with_a_rating_of_5(comedy, rating_mean):
    """
    Данная функция показывает комедии с средним рейтингом 4.7 и более.
    •	comedy: таблица с фильмами только определенного жанра
    •	rating_mean: таблица с средним рейтингом всех фильмов
    """
    # rating_mean_4_7 = rating_mean[rating_mean["rating"]>=4.7]
    # comedy_with_4_7 = rating_mean_4_7.merge(comedy, how = 'inner', left_on='movieId', right_on='movieId')
    # del comedy_with_4_7['year']


def old_movies_with_low_ratings(movies, rating_mean):
    """
    Данная функция показывает фильмы выпущенные раньше 2000 с средним рейтингом 3.4 и более.
    •	movies: таблица со всеми фильмами
    •	rating_mean: таблица с средним рейтингом всех фильмов
    """
    # old_movies=movies[movies["year"]<2000]
    # rating_mean_3_4=rating_mean[rating_mean["rating"]<3.4]
    # old_movies_3_4=rating_mean_3_4.merge(old_movies,how = 'inner', left_on='movieId', right_on='movieId')


def right_user_finding(genre, year, films, user):
    """
    суммирование рейтинга данных фильмов, данного пользователя,
    данного года, определение пользователя с наивысшей суммой
    """
