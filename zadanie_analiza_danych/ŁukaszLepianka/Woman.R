library(dplyr)
library(ggplot2)
library(stringr)
library(stringi)
library(tidyr)
library(reshape2)

df <- read.csv("Womens Clothing E-Commerce Reviews.csv")

# Ranking -----------------------------------------------------------------
df %>% 
  select(Department.Name, Class.Name, Rating) %>% 
  group_by(Department.Name, Class.Name) %>% 
  summarise(N = n(), Mean.Rating = mean(Rating)) %>% 
  filter(N > 20) %>%
  arrange(-N) %>% 
  filter(Department.Name != "Trend") -> temp

# Ilość recenzji dla poszczególnych kategorii
ggplot(temp, aes(x = N, y = Department.Name, fill = Department.Name)) +
  geom_col() +
  labs(title = "Rozkład recenzji w zależności od kategorii ubioru",
       x = "Liczba recenzji",
       y = "Kategoria ubrań")

# Ilość recenzji dla poszczególnych ubrań
ggplot(temp, aes(x = N, y = reorder(Class.Name, N), fill = Department.Name)) +
  geom_col() +
  labs(title = "Liczba recenzji dla danej części garderoby",
       x = "Ilość recenzji",
       y = "Część garderoby")

# Średnia ocena poszczególnych ubrań
ggplot(temp, aes(x = Mean.Rating , y = reorder(Class.Name, Mean.Rating), fill = Department.Name)) +
  geom_col() +
  coord_cartesian(xlim=c(4,4.5)) +
  labs(title = "Średnia ocena dla danej części garderoby",
       x = "Średnia ocena",
       y = "Część garderoby")

#Liczenie korelacji
mat <- cbind(temp$N, temp$Mean.Rating)
corelation <- round(cor(mat),2)
melted_cor <- melt(corelation)
ggplot(melted_cor, aes(x = Var1, y = Var2, fill = value)) +
  geom_tile() +
  geom_text(aes(label = value)) +
  scale_fill_gradient2(low = "red", mid ="white", high = "green", na.value = "black") +
  scale_x_discrete() +
  scale_y_discrete() +
  labs(title = "Korelacja między ilością recenzji a średnią oceną")

# Dystrybucja wieku -------------------------------------------------------

# Zliczanie wartości i średniej z ocen dla wieku
df %>% group_by(Age) %>% summarise(N= n(), Mean = mean(Rating)) %>%
  mutate(Age_interval = case_when( Age >= 20 & Age <=34 ~ "20-34",
                          Age >= 20 & Age <=49 ~ "35-49",
                          Age >= 50 ~ "50+")) -> temp

# Rozkład wieku
ggplot(temp, aes(x = Age, y = N, fill = Age_interval)) +
  geom_col() +
  coord_cartesian(xlim = c(21,75)) +
  labs(title = "Rozkład recenzji w zależności od wieku",
       x = "Wiek",
       y = "Liczba recenzji")

# Rozkład średniej w stosunku do wieku
ggplot(temp, aes(x = Age, y = Mean, fill = Age_interval)) +
  geom_col() +
  coord_cartesian(xlim = c(21,75), ylim = c(2.5,4.5)) +
  labs(title = "Rozkład średniej oceny w zależności od wieku",
       x = "Wiek",
       y = "Średnia ocena")


# Dane do wykresu - posegregowanie wieku
df %>%
  mutate(Age = case_when( Age >= 20 & Age <=34 ~ "20-34",
                          Age <=49 ~ "35-49",
                          Age >= 50 ~ "50+")) %>% 
  group_by(Age, Department.Name) %>% 
  summarise(N = n(), Mean = mean(Rating)) %>% 
  filter(N > 20 & Department.Name != "Trend") %>%
  arrange(-Mean)-> temp
#  Rysowanie wykresu
ggplot(temp, aes(x = Age, y = N, fill = reorder(Department.Name, N))) +
  geom_col(position = "dodge2") +
  labs(title = "Rozkład recenzji w zależności od wieku",
       x = "Wiek",
       y = "Liczba recenzji",
       fill = "Kategoria ubrań")
# Wartościowe recenzje [Positive - Feedback] ----------------------------------------------------

# Wyznaczanie długości recenzji
df %>% 
  arrange(-Positive.Feedback.Count) %>% 
  mutate(length = str_length(Review.Text)) %>% 
  arrange(-length) %>% 
  filter(Age >= 21, Age <= 65)-> temp

# Macierz 3 zmiennych do policzenia korelacji
mat <- cbind(temp$Positive.Feedback.Count, temp$length, temp$Age)

#Liczenie korelacji
corelation <- round(cor(mat),2)
melted_cor <- melt(corelation)

ggplot(melted_cor, aes(x = Var1, y = Var2, fill = value)) +
  geom_tile() +
  geom_text(aes(label = value)) +
  scale_fill_gradient2(low = "red", mid ="white", high = "green") +
  labs(title = "Współczynniki korelacji dla poszczególnych zmiennych",
       fill = "Wsp. Korelacji") +
  theme_classic()
  
# Wczytywanie słów -------------------------------------------------------------------

prepositions <- read.csv("prepositions-in-english.csv", col.names = c("Word","Meaning"))
pronouns <- read.csv("pronouns-in-english.csv", col.names = c("Word","Meaning"))
adverbs <- read.csv("adverbs-in-english.csv", col.names = c("Word","Meaning"))
conjunctions <- read.csv("conjunctions-in-english.csv", col.names = c("Word","Meaning"))
articles <- read.csv("articles-in-english.csv", col.names = c("Word","Meaning"))
adjectives <- read.csv("adjectives.csv")

# Słowa Pozytywne ----------------------------------------------------------

# Wydobycie pozytywnych recenzji
df %>% 
  filter(Recommended.IND == 1, Rating >= 3) -> positive

# Sparsowanie słów
slowa <- stri_trans_tolower(positive$Review.Text)
slowa <- stri_extract_all(slowa, regex = "[\\w']+")
slowa <- unlist(slowa)

# Zliczenie słów
df_slowa <- as.data.frame(slowa)
df_slowa %>% 
  group_by(slowa) %>% 
  summarise(N = n()) %>% 
  arrange(-N) -> sum_slowa

# Filtorowanie tych słów, które niosą ze sobą jakąś wartość (emocjonalną)
sum_slowa %>% 
  filter(!slowa %in% prepositions$Word) %>%
  filter(!slowa %in% pronouns$Word) %>%
  filter(!slowa %in% adverbs$Word) %>%
  filter(!slowa %in% conjunctions$Word) %>%
  filter(!slowa %in% articles$Word) %>%
  filter(slowa %in% adjectives$adjectives|
           slowa == "not") -> words_positive

write.csv(words_positive, file = "Positive.csv")
?write.table
# not = 7237
# % = 0.6531
# miejsce 3
100*7237/sum(sum_slowa$N)


# Słowa Negatywne ---------------------------------------------------------

# Wydobycie pozytywnych recenzji
df %>% 
  filter(Recommended.IND == 0, Rating <= 2) -> negative

# Sparsowanie słów
slowa <- stri_trans_tolower(negative$Review.Text)
slowa <- stri_extract_all(slowa, regex = "[\\w']+")
slowa <- unlist(slowa)

# Zliczenie słów
df_slowa <- as.data.frame(slowa)
df_slowa %>% 
  group_by(slowa) %>% 
  summarise(N = n()) %>% 
  arrange(-N) -> sum_slowa

# Filtorowanie tych słów, które niosą ze sobą jakąś wartość (emocjonalną)
sum_slowa %>%
  filter(!slowa %in% prepositions$Word) %>%
  filter(!slowa %in% pronouns$Word) %>%
  filter(!slowa %in% adverbs$Word) %>%
  filter(!slowa %in% conjunctions$Word) %>%
  filter(!slowa %in% articles$Word) %>%
  filter(slowa %in% adjectives$adjectives |
         slowa == "not") -> words_negative

write.csv(words_negative, "Negative.csv")

#not = 1380
# % = 1%
# miejsce 1

100*1380/sum(sum_slowa$N)

# Słowa w Pomocnych recenzjach --------------------------------------------

df %>% 
  filter(Positive.Feedback.Count > quantile(df$Positive.Feedback.Count,0.95)) -> helpful

slowa <- stri_trans_tolower(helpful$Review.Text)
slowa <- stri_extract_all(slowa, regex = "[\\w']+")
slowa <- unlist(slowa)

# Zliczenie słów
df_slowa <- as.data.frame(slowa)
df_slowa %>% 
  group_by(slowa) %>% 
  summarise(N = n()) %>% 
  arrange(-N) -> sum_slowa

# Filtorowanie tych słów, które niosą ze sobą jakąś wartość (emocjonalną)
sum_slowa %>%
  filter(!slowa %in% prepositions$Word) %>%
  filter(!slowa %in% pronouns$Word) %>%
  filter(!slowa %in% adverbs$Word) %>%
  filter(!slowa %in% conjunctions$Word) %>%
  filter(!slowa %in% articles$Word) %>%
  filter(slowa %in% adjectives$adjectives |
           slowa == "not") -> words_helpful