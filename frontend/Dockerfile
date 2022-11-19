FROM node:18

COPY . .

WORKDIR ./mobile-photo-frontend

ENV imageURL="https://codes.binary141.com/"

RUN sed -i "s%defaultURL%${imageURL}%g" src/views/Tab1Page.vue
RUN sed -i "s%defaultURL%${imageURL}%g" src/views/Tab2Page.vue

RUN npm install

EXPOSE 8080

CMD ["npm", "run", "serve", "--lab-host=0.0.0.0", "--external", "--host=0.0.0.0"]
