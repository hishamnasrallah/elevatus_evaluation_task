const dbName = process.env.DB_NAME
const username = process.env.DB_USERNAME
const password = process.env.DB_PASSWORD

db = db.getSiblingDB(dbName)


db.createUser({
    user: username,
    pwd: password,
    roles: [
      {
        role: 'dbOwner',
      db: dbName,
    },
  ],
});