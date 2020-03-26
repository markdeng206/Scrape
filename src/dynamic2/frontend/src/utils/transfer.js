const secretKey = 'ef34#teuq0btua#(-57w1q5o5--j@98xygimlyfxs*-!i-0-mb'
const CryptoJS = require('crypto-js')

function transfer(string) {
  console.log('stttt', string)
  return CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(secretKey + string))
}

export default transfer