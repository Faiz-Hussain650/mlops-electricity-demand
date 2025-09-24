provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "mlops_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "mlops_subnet" {
  vpc_id     = aws_vpc.mlops_vpc.id
  cidr_block = "10.0.1.0/24"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "mlops-cluster"
  cluster_version = "1.27"
  subnets         = [aws_subnet.mlops_subnet.id]
  vpc_id          = aws_vpc.mlops_vpc.id
}
