provider "aws" {
  region = "us-east-1"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "mlops-cluster"
  cluster_version = "1.27"
  vpc_id          = "vpc-xxxx"        # replace with your VPC
  subnets         = ["subnet-xxxx"]   # replace with your subnets
}
