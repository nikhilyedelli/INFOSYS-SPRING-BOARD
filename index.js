const express = require('express')
const app = express()
const port = 3000
app.get('/',(req,res)=> res.send('welcome to new server'))
app.listen(3000,()=>console.log('app listening on port 3000!..'))
    