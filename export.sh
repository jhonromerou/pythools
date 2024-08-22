
# copiar env
mv .env .env_backup
mv example.env .env

zip -r pythools.zip src/ .gitignore .env

#restaurar ennv
mv .env example.env
mv .env_backup .env
