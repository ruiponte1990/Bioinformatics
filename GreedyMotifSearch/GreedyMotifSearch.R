score <- function(Motifs) {
  score <- 0
  k <- nchar(Motifs[1])
  t <- length(Motifs)
  
  for (i in 1:k) {
    Counts <- c(0, 0, 0, 0)
    
    for (j in 1:t) {
      if (substring(Motifs[j], i, i) == "A") {
        Counts[1] <- Counts[1] + 1
      } else if (substring(Motifs[j], i, i) == "C") {
        Counts[2] <- Counts[2] + 1
      } else if (substring(Motifs[j], i, i) == "G") {
        Counts[3] <- Counts[3] + 1
      } else{
        Counts[4] <- Counts[4] + 1
      }
    }
    score <- score + (t - max(Counts))
    
  }
  return(score)
}

profile_most_probable <- function(Profile, DNA, k) {
  p = 0
  numMers <- (nchar(DNA) - k + 1)
  bestMer <- ""

  for (i in 1:numMers) {
    end <- i + k - 1
    kmer <- substring(DNA, i, end)

    pbegin = 1
    for (j in 1:k) {

      if (substring(kmer, j, j) == "A") {
        pbegin <- pbegin * Profile[1, j]
      } else if (substring(kmer, j, j) == "C") {
        pbegin <- pbegin * Profile[2, j]
      } else if (substring(kmer, j, j) == "G") {
        pbegin <- pbegin * Profile[3, j]
      } else{
        pbegin <- pbegin * Profile[4, j]
      }
    }

    if (pbegin > p) {
      p <- pbegin
      bestMer <- kmer
      
    }
  }

  return(bestMer)
}

make_profile <- function(Motifs) {

  k <- nchar(Motifs[1])
  t <- length(Motifs)
  h <- 1 / (t + 4)
  profile <- matrix(h, 4, k)
  for (i in 1:k) {
    for (j in 1:t) {
      if (substring(Motifs[j], i, i) == "A") {
        profile[1, i] <- profile[1, i] + h
      } else if (substring(Motifs[j], i, i) == "C") {
        profile[2, i] <- profile[2, i] + h
      } else if (substring(Motifs[j], i, i) == "G") {
        profile[3, i] <- profile[3, i] + h
      } else{
        profile[4, i] <- profile[4, i] + h
      }
    }
  }
  return(profile)
}

input <- file("rosalind_ba2e.txt", open = "r")
line = readLines(input)
x <- strsplit(line[1], " ")
k <- as.numeric(x[[1]][1])
t <- as.numeric(x[[1]][2])
BestMotifs <- character(t)
for (i in 2:length(line)) {
  BestMotifs[i - 1] <- substring(line[i], 1, k)
}
numMers <- nchar(line[2]) - k + 1
Motifs <- character(t)
for (i in 1:numMers) {
  Motifs[1] <- substring(line[2], i, i + k - 1)
  
  for (j in 2:t) {
    profile_motifs <- character(j - 1)
    for (z in 1:j - 1) {
      profile_motifs[z] <- Motifs[z]
    }
 
    profile <- make_profile(profile_motifs)

    Motifs[j] <- profile_most_probable(profile, line[j + 1], k)
  }
  
  if (score(Motifs) < score(BestMotifs)) {
   

    BestMotifs <- Motifs
    
  }
}

for(i in 1:length(BestMotifs)){
   cat(BestMotifs[i])
   cat("\n")
  }

