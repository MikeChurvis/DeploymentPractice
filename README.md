# Deployment Practice

In this practice project I take a full stack web app in a development environment and deploy it to a DigitalOcean droplet. I'm doing this so that I don't botch my portfolio website's actual deployment.

## Musings

### .env files

In a perfect world I'd have a single source of truth for all variables that are shared by different parts of the project. For example, maximum field length validation: as the moment there is no hard link between the max field length value used by the validators on the frontend and the validators on the backend. I have to manually mirror those changes. This is a tedious and error-prone dev experience.

I need a global config. My gut says to make an `.env/` folder at the project root level and populate it with the .env files needed throughout my project.

Pros:
- docker-compose can effortlessly distribute these .env files to the containers that need them.

Cons:
- Vite uses dotenv to read an .env file from the *Astro* project root, not the global project root. I'd need a way to either point dotenv at an .env file in a different directory, or somehow get the `env/.env-astro` file auto-copied or hard-linked into the Astro project root. (I think I just answered my own question: hard-link the .env-astro file)
- If I'm using multiple .env files then I'm still not using a *single* source of truth. I need something that generates the .env files on-the-fly from a single config file. A custom git command, perhaps? Node script? I'll think about it.

## Snippets

`docker compose run app django-admin startproject django_project .`

## Reference Material

- [Docker Compose file reference](https://docs.docker.com/compose/compose-file/compose-file-v3/.)
- [Docker GitHub CI/CD tutorial](https://testdriven.io/blog/deploying-django-to-digitalocean-with-docker-and-github-actions/#project-setup)

