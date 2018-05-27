#!/usr/bin/python
# -*- coding: utf-8 -*-
import webbrowser


class Movie:

    """The Movie class stores the title,story,poster URL and Trailer."""

    def __init__(
        self,
        movie_title,
        movie_storyline,
        poster_image,
        trailer_youtube,
        ):
        """Initialize the instances of the class."""

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Method to show the trailer of the movie

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)



			