const CryptoJS = require('crypto-js')
const key = 'Germey'
var SHA1 = require("crypto-js/sha1");

function encrypt(...args) {
  let time = Math.round(new Date().getTime() / 1000).toString()
  args.push(time)
  console.log('args.join(\',\')', args.join(','))
  let sign = CryptoJS.SHA1(args.join(',')).toString(CryptoJS.enc.Hex)
  console.log('sign', sign)
  console.log('sign2', SHA1(args.join(',')).toString())
  let string = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse([sign, time].join(',')))
  console.log('token', string)
  // let token = CryptoJS.AES.encrypt(string, key).iv.toString(CryptoJS.enc.Hex)
  // console.log('token', token)
  return string
}

export default encrypt;