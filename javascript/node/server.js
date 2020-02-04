const express = require('express')
const bodyParser = require('body-parser')
//const router = express.Router()
const router = require('./network/routes')
//const response = require('./network/response')

let app = express()

// app.use('/', (req, res) => res.send('Hola Mundo'))

app.use(bodyParser.json())
//app.use(router)
router(app)
app.use('/app', express.static('./public'))



app.listen(3000)

console.log('La aplicación está escuchando en http://localhost:3000')