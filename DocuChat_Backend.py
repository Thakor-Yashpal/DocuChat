from pydantic import BaseModel
import pymongo
# Import traceback for error handling
import traceback

# Import os and sys for system-related operations
import os, sys
import traceback  # Import traceback for error handling
from fastapi import (
    FastAPI,
    UploadFile,
    status,
    HTTPException,
)  # Import FastAPI components for building the web application
from fastapi.responses import JSONResponse  # Import JSONResponse for returning JSON responses
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware to handle Cross-Origin Resource Sharing
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
# from langchain_community.document_loaders import S3FileLoader
from langchain_community.document_loaders import Docx2txtLoader,PyPDFLoader


from langchain_community.callbacks import get_openai_callback
from langchain.chains import ConversationalRetrievalChain

from langchain_openai import ChatOpenAI
import gc

import urllib.parse
import awswrangler as wr  # Import AWS Wrangler for working with AWS services

import boto3  # Import the boto3 library for interacting with AWS services

# Import the OS module for system-related operations

# Check if the operating system is Windows
if os.name == "nt":  # Windows
    # If it's Windows, import the `load_dotenv` function from the `dotenv` library
    from dotenv import load_dotenv

    # Load environment variables from a `.secrets.env` file (used for local development)
    load_dotenv(".secrets.env")
