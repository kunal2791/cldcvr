terraform {
  backend "s3" {
    bucket = "cloud-cover-assignment-terraform"
    region = "us-east-1"
    key    = "nonprod/us-east-1/eks/eks.tfstate"
  }
}