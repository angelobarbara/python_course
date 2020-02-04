const express = require('express')
const router = express.Router()
const response = require('../../network/response')

router.get('/', function (req, res) {
    // if(req.query.error){
    //     response.error(req,res,'Error',400)
    // }else{
    //     response.success(req,res,'Lista de mensajes')
    // }

    req.query.error ? response.error(req, res, 'Error simulado', 400) : response.success(req, res, 'Lista de mensajes')
})

//router.post('/', (req, res) => response.success(req, res, 'Creado correctamente', 201))
router.post('/', function (req, res) {
    req.query.error ? response.error(req, res, 'Error simulado', 400) : response.success(req, res, 'Creado correctamente', 201)
})

module.exports = router