# main.tf
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "my_ec2" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2 AMI (example)
  instance_type = "t2.micro"
  key_name      = var.key_name
  tags = {
    Name = "MyEC2Instance"
  }
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = var.bucket_name
  acl    = "public-read"
  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}
