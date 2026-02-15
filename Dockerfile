# Use official Nginx image
FROM nginx:alpine

# Remove default nginx content
RUN rm -rf /usr/share/nginx/html/*

# Copy your website files into nginx folder
COPY . /usr/share/nginx/html

# Expose port 80 to the outside
EXPOSE 80

# Start nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
