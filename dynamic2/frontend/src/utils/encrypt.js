const CryptoJS = require('crypto-js')

function encrypt(...args) {
  let time = Math.round(new Date().getTime() / 1000).toString()
  args.push(time)
  let sign = CryptoJS.SHA1(args.join(',')).toString(CryptoJS.enc.Hex)
  let string = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse([sign, time].join(',')))
  return string
}

export default encrypt;