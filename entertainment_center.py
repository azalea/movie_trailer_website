from media import Movie
import fresh_tomatoes

# Hard code movies to be displayed on the website below
furious1 = Movie('The Fast and the Furious',
                 'Los Angeles police officer Brian O\'Connor must decide where his loyalties really lie when he becomes enamored with the street racing world he has been sent undercover to destroy.',
                  'http://ia.media-imdb.com/images/M/MV5BMjAwNTQ0Nzc2M15BMl5BanBnXkFtZTcwNTk1MDIwNA@@._V1_SX214_AL_.jpg',
                  'https://www.youtube.com/watch?v=lTRftZx2tAo')
furious2 = Movie('2 Fast 2 Furious',
                 'Brian O\'Conner and childhood friend Roman Pearce are re-united by the FBI to bring down a Miami drug exporter in exchange for clear records.',
                 'http://ia.media-imdb.com/images/M/MV5BMTIyMDUwMDc4OF5BMl5BanBnXkFtZTYwNTY2Nzk5._V1_SX214_AL_.jpg',
                 'https://www.youtube.com/watch?v=EyCtnA15PRc')
furious3 = Movie('The Fast and the Furious: Tokyo Drift',
                 'A teenager becomes a major competitor in the world of drift racing after moving in with his father in Tokyo to avoid a jail sentence in America.',
                 'http://ia.media-imdb.com/images/M/MV5BMTQ2NTMxODEyNV5BMl5BanBnXkFtZTcwMDgxMjA0MQ@@._V1_SY317_CR0,0,214,317_AL_.jpg',
                 'https://www.youtube.com/watch?v=p8HQ2JLlc4E')
furious4 = Movie('Fast & Furious',
                 'Brian O\'Conner, now working for the FBI in LA, teams up with Dominic Toretto to bring down a heroin importer by infiltrating his operation.',
                 'http://ia.media-imdb.com/images/M/MV5BMTQwNDA2MTg3Nl5BMl5BanBnXkFtZTcwNTg3MzIyMg@@._V1_SY317_CR1,0,214,317_AL_.jpg',
                 'https://www.youtube.com/watch?v=bcY7HkvF1aw')
furious5 = Movie('Fast Five',
                 'Dominic Toretto and his crew of street racers plan a massive heist to buy their freedom while in the sights of a powerful Brazilian drug lord and a dangerous federal agent.',
                 'http://ia.media-imdb.com/images/M/MV5BMTUxNTk5MTE0OF5BMl5BanBnXkFtZTcwMjA2NzY3NA@@._V1_SY317_CR0,0,214,317_AL_.jpg',
                 'https://www.youtube.com/watch?v=bf4oDjHUmkY')
furious6 = Movie('Fast & Furious 6',
                 'Hobbs has Dominic and Brian reassemble their crew to take down a team of mercenaries: Dominic unexpectedly gets convoluted also facing his presumed deceased girlfriend, Letty.',
                 'http://ia.media-imdb.com/images/M/MV5BMTM3NTg2NDQzOF5BMl5BanBnXkFtZTcwNjc2NzQzOQ@@._V1_SX214_AL_.jpg',
                 'https://www.youtube.com/watch?v=l2h75LLhxM4')
furious7 = Movie('Furious 7',
                 'Deckard Shaw seeks revenge against Dominic Toretto and his family for his comatose brother.',
                 'http://ia.media-imdb.com/images/M/MV5BMTQxOTA2NDUzOV5BMl5BanBnXkFtZTgwNzY2MTMxMzE@._V1_SX214_AL_.jpg',
                 'https://www.youtube.com/watch?v=Skpu5HaVkOc')

# Call fresh_tomatoes.open_movies_page() with the list of movies 
fresh_tomatoes.open_movies_page([furious1, furious2, furious3, furious4, furious5, furious6, furious7])




