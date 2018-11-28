generate_kmer <- function(Profile, DNA, k) {
  numMers <- nchar(DNA) - k + 1
  mers <- character(numMers)
  probabilities <- numeric(numMers)
  for (i in 1:numMers) {
    end <- i + k - 1
    kmer <- substring(DNA, i, end)
    mers[i] <- kmer
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
    probabilities[i] <- pbegin
    
  }
  
  s <- sum(probabilities)
  for (i in 1:numMers) {
    probabilities[i] <- probabilities[i] / s
  }
  #print("Probabilities")
  #print(probabilities)
  #print("Sum of Probabilities")
  #print(sum(probabilities))
  return_mer <- sample(mers, replace = FALSE, prob = probabilities)
  return(return_mer)
}

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

input <- file("gibbstest.txt", "r")
line = readLines(input)
x <- strsplit(line[1], " ")
k <- as.numeric(x[[1]][1])
t <- as.numeric(x[[1]][2])
N <- as.numeric(x[[1]][3])
Motifs <- character(t)
numMers <- nchar(line[2]) - k + 1
scoreOut <- Inf
finalMotifs <- Motifs
for (y in 1:20) {
  for (i in 2:length(line)) {
    z <- sample(1:numMers, 1)
    Motifs[i - 1] <- substring(line[i], z, z + k)
  }
  BestMotifs <- Motifs
  for (j in 1:N) {
    i <- sample(1:t, 1)
    profile_motifs <- character(t - 1)
    index <- 1
    for (h in 1:t) {
      if (h != i) {
        profile_motifs[index] <- Motifs[h]
        index <- index + 1
      }
    }
    
    profile <- make_profile(profile_motifs)
    Motifs[i] <- generate_kmer(profile, line[i + 1], k)
    if (score(Motifs) < score(BestMotifs)) {
      BestMotifs <- Motifs
      if(score(BestMotifs) < scoreOut){
        scoreOut <- score(BestMotifs)
        finalMotifs <- BestMotifs
      }
    }
  }
  
}
for (i in 1:length(finalMotifs)) {
  cat(finalMotifs[i])
  cat("\n")
}
