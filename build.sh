# Set the name of your Docker image
IMAGE_NAME="my-streamlit-app"

# Set the port for Streamlit (default is 8501)
PORT=8501

# Step 1: Build the Docker image
echo "Building Docker image..."
docker build -t $IMAGE_NAME .

# Check if the build was successful
if [ $? -eq 0 ]; then
    echo "Docker image built successfully!"
else
    echo "Docker build failed. Exiting."
    exit 1
fi

# Step 2: Run the Docker container
echo "Running Docker container..."
docker run -p $PORT:8501 $IMAGE_NAME

# Check if the container is running
if [ $? -eq 0 ]; then
    echo "Streamlit app is running on http://localhost:$PORT"
else
    echo "Failed to start Docker container. Exiting."
    exit 1
fi
