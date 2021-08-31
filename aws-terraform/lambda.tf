locals {
    lambda-zip-location = "outputs/WebScraping.zip"
}

data "archive_file" "init" {
  type        = "zip"
  source_files = ["WebScraping.py", "Ulta_WS.py"]
  output_path = local.lambda-zip-location
}

resource "aws_lambda_function" "test_lambda" {
  filename      = local.lambda-zip-location
  function_name = "WebScraping"
  role          = aws_iam_role.lambda_role.arn
  handler       = "WebScraping.main"

  runtime = "python3.7"
}