# Project Title

Application gathers additional information about movie based on movie title

## Getting Started

For download:

```
git clone https://github.com/wojciezki/movie_info.git
```

### Prerequisites

Installing and activate virtualenv:

```
python3.6 -m venv venv_movies
. venv_movies/bin/activate
```

Installing packages:

```
cd movie_info
pip install -r requirements.txt
```

## Running application

In application root folder type (in terminal)

```
python manage.py runserver
```

## Running the tests

To run test type in terminal in app root folder:

```
python manage.py test
```

## Filtering options

The are several filtering options on each views:

/movie/  --  'title', 'year', 'actors', 'country'

Examples:

/movie/?title=Avatar
/movie/?title__icontains=Jungle

/comments/ -- 'movie'

Examples:
/comments/?movie=[movie_id]

/top/ -- date range -> date_from and date_to

Examples:
/top/?date_from=2018-01-01&date_to=2019-01-01

## License

This project is licensed under the MIT License
