import media
import fresh_tomatoes

bill_ted = media.Movie("Bill & Ted's Excellent Adventure", 
						"1989",
						"Two seemingly dumb teens struggle to prepare a historical presentation with the help of a time machine.",
						 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk3Mjk5MzI3OF5BMl5BanBnXkFtZTcwMTY4MzcyNA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
						 "https://www.youtube.com/watch?v=sFy17auuK08")

deadpool = media.Movie("Deadpool", 
						"2016",
						"A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge.",
						 "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_UY268_CR1,0,182,268_AL_.jpg",
						 "https://www.youtube.com/watch?v=Rz4AqfIAqnY")

blues = media.Movie("The Blues Brothers", 
						"1980",
						"Jake Blues, just out from prison, puts together his old band to save the Catholic home where he and brother Elwood were raised.",
						 "https://images-na.ssl-images-amazon.com/images/M/MV5BMzdhOTJmYmQtMmE0OS00ZDMyLWFkZDItZmZmMGJlNGUyNjNhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg",
						 "https://www.youtube.com/watch?v=2HCR4c1zPyk")

gump = media.Movie("Forrest Gump", 
						"1994",
						"While not intelligent, Forrest Gump has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
						 "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UY268_CR10,0,182,268_AL_.jpg",
						 "https://www.youtube.com/watch?v=uPIEn0M8su0")

intersteller = media.Movie("Interstellar", 
						"2014",
						"A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
						 "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
						 "https://www.youtube.com/watch?v=zSWdZVtXT7E")

spencer = media.Movie("Zwei ausser Rand und Band", 
						"1977",
						"An attempted robbery turns to be an unexpected recruitment when two unemployed men mistakenly break into a police office instead of a store.",
						 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkwMDU4OTkyMV5BMl5BanBnXkFtZTcwMzIxMTU0MQ@@._V1_UY268_CR1,0,182,268_AL_.jpg",
						 "https://www.youtube.com/watch?v=PWbjj2o655U")

movies = {spencer, blues, bill_ted, gump, intersteller, deadpool}
fresh_tomatoes.open_movies_page(movies)	