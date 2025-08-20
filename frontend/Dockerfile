FROM node:20

WORKDIR /app/frontend

COPY package*.json ./
COPY vite.config.ts ./

EXPOSE 5173

RUN npm install && \
    npm install tailwindcss @tailwindcss/vite

COPY . .

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]