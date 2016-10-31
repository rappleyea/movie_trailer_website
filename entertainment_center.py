import fresh_tomatoes
import media

bourne_identity = media.Movie("The Bourne Identity (2002)",
                              "A secret agent wakes up to find that he does not remember who he is",
                              "http://www.joblo.com/timthumb.php?src=/posters/images/full/2002-bourne_"
                              "identity-2.jpg&h=600&q=100",
                              "https://www.youtube.com/watch?v=FpKaB5dvQ4g", )

die_hard = media.Movie("Die Hard (1988)",
                       "A classic Christmas story with guns",
                       "http://www.geeksofdoom.com/GoD/img/2013/12/die-hard-movie-poster-1988.jpg",
                       "https://www.youtube.com/watch?v=2TQ-pOvI6Xo", )

good_bye_lenin = media.Movie("Good Bye, Lenin! (2003)",
                             "An East Berliner shields his mother from the realities of German reunification",
                             "https://www.movieposter.com/posters/archive/main/60/MPW-30406",
                             "https://www.youtube.com/watch?v=iJb4efZcFUM", )

naked_gun = media.Movie("The Naked Gun (1988)",
                            "An incompetent cop tries to foil an assassination attempt",
                            "http://bedfordfilmfestival.org/wp-content/uploads/2015/08/The-Naked-Gun-poster.jpg",
                            "https://www.youtube.com/watch?v=PACTQutbow4", )

spinal_tap = media.Movie("This is Spinal Tap (1984)",
                         "A has-been rock band stumbles their way through a US tour",
                         "http://www.joblo.com/timthumb.php?src=/posters/images/full/1984-this-is-spinal-tap-poster1."
                         "jpg&h=600&q=100",
                         "https://www.youtube.com/watch?v=N63XSUpe-0o", )

when_harry_met_sally = media.Movie("When Harry Met Sally (1989)",
                                  "Two friends look for love in 1980s New York",
                                  "http://www.impawards.com/1989/posters/when_harry_met_sally_xxlg.jpg",
                                  "https://www.youtube.com/watch?v=V8DgDmUHVto", )

movies = [bourne_identity, die_hard, good_bye_lenin, naked_gun, spinal_tap, when_harry_met_sally]
fresh_tomatoes.open_movies_page(movies)



