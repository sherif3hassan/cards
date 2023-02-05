# Cards Against Humanity Clone 

## Table of contents

- [Overview](#overview)
- [Why ditch Deta Cloud?](#why-ditch-deta-cloud)
- [To Dos](#to-dos)

## Overview

> [Cards Against Humanity](https://www.cardsagainsthumanity.com/) is a fill-in-the-blank party game that turns your awkward personality and lackluster social skills into hours of fun!

This is a free clone of the original game, made using
[FastAPI](https://fastapi.tiangolo.com).

Originally, we deployed the game to [Deta Cloud](https://web.deta.sh), but the platform was very limited for our needs (See [Why ditch Deta Cloud?](#why-ditch-deta-cloud)), so we switched to [Render](https://render.com/).

## Why ditch Deta Cloud?

Deta allowed us to deploy the FastAPI micro easily, it was quick and efficient, but the problem was that we really wanted to use [WebSockets](https://en.wikipedia.org/wiki/WebSocket) to connect users to the game, and Deta micros had a 10-seconds timeout, which
made it imposible to update users with the latest game state.

Initially, we tried overcoming this limitation by avoiding
WebSockets, and tried using [Long Polling](https://en.wikipedia.org/wiki/Push_technology#Long_polling) instead, but of course,
this approach had its own limitations.

After ditching Deta Cloud and switching to Render, we were
able to use WebSockets, but faced another problem, that is
Render's free plan is extremely slow in deployment.

So, we used [Railway](https://railway.app/) to deploy and test
the game, and when we were happy with the result, we deploy to
Render.

## To Dos

- Allow users to create their own custom packs.
