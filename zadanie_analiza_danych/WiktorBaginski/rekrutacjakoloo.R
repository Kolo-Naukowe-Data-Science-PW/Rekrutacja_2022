library(data.table)
library(ggthemes)
library(ggplot2)
setwd("C:\\Users\\RossRozwodnik\\Desktop\\uczelnia\\kolo")

summer_prod <- read.csv("summer-products.csv")
summary(summer_prod)

summer_prod <- as.data.table(summer_prod)



price_sorter <- function(x) {
  stopifnot(is.numeric(x))
  p <- ifelse(x<5, "under 5", ifelse(
    x<20, "5-20", "20+"
  ))
  p
}
library(stringi)

unitstags <- function(){
  try1 <- summer_prod
  try1 <- try1[, is_sexy:= .(stri_detect_fixed(paste(as.character(title),as.character(title_orig)), "sexy")
                             | stri_detect_fixed(paste(as.character(title), as.character(title_orig)), "Sexy"))]
  try1 <- try1[, num_tags:= .(stri_count_regex(tags, ","))]
  unitspertagstable <- try1[, .(mean(units_sold)), by= .(num_tags)]
  unitspertagstable
}

unitspertagstable <- unitstags()
unitspertags <- ggplot(unitspertagstable, aes(x= num_tags, y= V1)) + 
  geom_line(size = 1.5) + labs(title = "Sprzeda¿ od liczby tagów",
                         x= "Liczba tagów",
                         y= "Iloœæ sprzedanych produktów") +
              theme_fivethirtyeight() + theme(axis.title = element_text())+
        scale_color_manual(values ="#9966CC")

sort_rating <- function(X) {
  stopifnot(is.numeric(X))
  X <- ifelse(X<2.5, "below 2.5", 
              ifelse(X<3, 2.5,
              ifelse(X<3.5, 3,
                     ifelse(X<4, 3.5,
                            ifelse(X<4.5, 4,
                                   ifelse(X<5, 4.5, 5))))))
  X
}

percent_stars <- function() {
  dt <- summer_prod
  dt <- dt[rating_count > 10]
  dt <- dt[, rating_type:= .(sort_rating(rating))]
  dt <- dt[order(rating)]
  dt <- dt[, .(percent_five= sum(rating_five_count)/sum(rating_count),
               percent_four= sum(rating_four_count)/sum(rating_count),
               percent_three= sum(rating_three_count)/sum(rating_count),
               percent_two= sum(rating_two_count)/sum(rating_count),
               percent_one= sum(rating_one_count)/sum(rating_count)),
           by= .(rating_type)]
  dt
}

stars <- percent_stars()

stars_plot_five <- ggplot(stars, aes(rating_type, percent_five)) +
  geom_line(size = 1.5) + labs(title = "Konkretne ratingi",
                             x= "Œredni rating",
                             y= "Iloœæ pi¹tek") +
  theme_fivethirtyeight() + theme(axis.title = element_text())

stars_plot_four <- ggplot(stars, aes(rating_type, percent_four)) +
  geom_line(size = 1.5) + labs(title = "Konkretne ratingi",
                               x= "Œredni rating",
                               y= "Iloœæ czwórek") +
  theme_fivethirtyeight() + theme(axis.title = element_text())

stars_plot_three <- ggplot(stars, aes(rating_type, percent_three)) +
  geom_line(size = 1.5) + labs(title = "Konkretne ratingi",
                               x= "Œredni rating",
                               y= "Iloœæ trójek") +
  theme_fivethirtyeight() + theme(axis.title = element_text())

stars_plot_two <- ggplot(stars, aes(rating_type, percent_two)) +
  geom_line(size = 1.5) + labs(title = "Konkretne ratingi",
                               x= "Œredni rating",
                               y= "Iloœæ dwójek") +
  theme_fivethirtyeight() + theme(axis.title = element_text())

stars_plot_one <- ggplot(stars, aes(rating_type, percent_one)) +
  geom_line(size = 1.5) + labs(title = "Konkretne ratingi",
                               x= "Œredni rating",
                               y= "Iloœæ jedynek") +
  theme_fivethirtyeight() + theme(axis.title = element_text())











                       