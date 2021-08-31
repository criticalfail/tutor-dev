FROM docker.io/node:12-alpine AS base

RUN apk add --no-cache \
    git \
    # npm package system dependencies
    autoconf \
    automake \
    build-base \
    libpng-dev \
    pngquant

RUN mkdir -p /openedx/app
WORKDIR /openedx/app

ENV PATH ./node_modules/.bin:${PATH}

# Create environment file directories
RUN mkdir -p /openedx/env


######## ecommerce (dev)
FROM base AS ecommerce-dev
RUN git clone https://github.com/edx/frontend-app-ecommerce --branch open-release/lilac.2 --depth 1 .
ARG NPM_REGISTRY=https://registry.npmjs.org/
RUN npm install --verbose --registry=$NPM_REGISTRY
ENV PUBLIC_PATH='/ecommerce/'
######## ecommerce (production)
FROM ecommerce-dev AS ecommerce
COPY ./env/production /openedx/env/production

RUN sh -c "set -a && source /openedx/env/production && npm run build"

######## payment (dev)
FROM base AS payment-dev
RUN git clone https://github.com/edx/frontend-app-payment --branch open-release/lilac.2 --depth 1 .
ARG NPM_REGISTRY=https://registry.npmjs.org/
RUN npm install --verbose --registry=$NPM_REGISTRY
ENV PUBLIC_PATH='/payment/'
######## payment (production)
FROM payment-dev AS payment
COPY ./env/production /openedx/env/production

ENV SUPPORT_URL=http://local.overhang.io/contact

RUN sh -c "set -a && source /openedx/env/production && npm run build"

######## account (dev)
FROM base AS account-dev
RUN git clone https://github.com/edx/frontend-app-account --branch open-release/lilac.2 --depth 1 .
ARG NPM_REGISTRY=https://registry.npmjs.org/
RUN npm install --verbose --registry=$NPM_REGISTRY
ENV PUBLIC_PATH='/account/'
######## account (production)
FROM account-dev AS account
COPY ./env/production /openedx/env/production

ENV COACHING_ENABLED=

ENV ENABLE_DEMOGRAPHICS_COLLECTION=

RUN sh -c "set -a && source /openedx/env/production && npm run build"

######## gradebook (dev)
FROM base AS gradebook-dev
RUN git clone https://github.com/edx/frontend-app-gradebook --branch open-release/lilac.2 --depth 1 .
ARG NPM_REGISTRY=https://registry.npmjs.org/
RUN npm install --verbose --registry=$NPM_REGISTRY
ENV PUBLIC_PATH='/gradebook/'
######## gradebook (production)
FROM gradebook-dev AS gradebook
COPY ./env/production /openedx/env/production

RUN sh -c "set -a && source /openedx/env/production && npm run build"

######## profile (dev)
FROM base AS profile-dev
RUN git clone https://github.com/edx/frontend-app-profile --branch open-release/lilac.2 --depth 1 .
ARG NPM_REGISTRY=https://registry.npmjs.org/
RUN npm install --verbose --registry=$NPM_REGISTRY
ENV PUBLIC_PATH='/profile/'
######## profile (production)
FROM profile-dev AS profile
COPY ./env/production /openedx/env/production

RUN sh -c "set -a && source /openedx/env/production && npm run build"


####### final production image with all static assets
FROM docker.io/caddy:2.3.0-alpine

RUN mkdir -p /openedx/dist

# Copy static assets

COPY --from=ecommerce /openedx/app/dist /openedx/dist/ecommerce

COPY --from=payment /openedx/app/dist /openedx/dist/payment

COPY --from=account /openedx/app/dist /openedx/dist/account

COPY --from=gradebook /openedx/app/dist /openedx/dist/gradebook

COPY --from=profile /openedx/app/dist /openedx/dist/profile


# Copy caddy config file
COPY ./Caddyfile /etc/caddy/Caddyfile