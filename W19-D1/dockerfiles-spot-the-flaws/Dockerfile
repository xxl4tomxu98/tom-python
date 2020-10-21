FROM node:10-alpine

WORKDIR /app

RUN DEBIAN_FRONTEND=noninteractive

COPY package.json .
RUN npm install
COPY . .

CMD ["npm", "start"]
