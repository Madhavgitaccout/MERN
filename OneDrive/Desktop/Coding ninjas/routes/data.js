const express = require('express');

const router = express.Router();
const dataController = require('../controllers/data_controller');


router.get('/info', dataController.data);


module.exports = router;