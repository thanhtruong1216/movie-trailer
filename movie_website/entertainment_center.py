import fresh_tomatoes
import media
white_princess = media.Movie("White Princess",
  "http://image.phimmoi.net/film/5216/poster.medium.jpg",
  "https://www.youtube.com/watch?v=TJ-q3_b3dkI")

once_upon_atime = media.Movie("Once Upon A Time",
   "https://images-na.ssl-images-amazon.com/images/I/91%2Brwb%2BDzzL.jpg",
   "https://www.youtube.com/watch?v=tQT90enuZc4")

the_lord_of_the_ring = media.Movie("The Lord Of The Rings",
  "http://static1.dienanh.net/upload/2015/03/12/the-lord-of-the-rings-the-fellowship-of-the-ring-22044.jpg",
  "https://www.youtube.com/watch?v=rCZ3SN65kIs")

game_of_thrones = media.Movie("Game Of Thrones",
  "http://image.phimmoi.net/film/5022/poster.medium.jpg",
  "https://www.youtube.com/watch?v=mg2xtVYgQhI")

hunger_game = media.Movie("Hunger Game",
   "https://photo.tinhte.vn/store/2014/11/2647018_Los-Juegos-del-Hambre-Sinsajo-Poster-Oficial-Empeliculados.co_.jpg",
   "https://www.youtube.com/watch?v=xPug6IJSKXs")

the_hundred = media.Movie("The Hundred",
  "https://s-media-cache-ak0.pinimg.com/originals/8c/75/c3/8c75c3bc83d45fa655f5d0d66066c23b.jpg",
  "https://www.youtube.com/watch?v=Iw7VtA6Pey0"
  )

movies = [white_princess, the_lord_of_the_ring, hunger_game, game_of_thrones, the_hundred, once_upon_atime]
fresh_tomatoes.open_movies_page(movies)
