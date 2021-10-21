FROM ruby:2.5.0-alpine

WORKDIR "/opt/katas"

RUN apk add --no-cache build-base libffi-dev

COPY Gemfile* $WORKDIR/
RUN  bundle install

COPY . $WORKDIR/

CMD ["bundle", "exec", "guard", "start", "-cipB"]
