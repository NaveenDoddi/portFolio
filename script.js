const toBase64 = obj => {
    const str = JSON.stringify (obj);
    console.log(Buffer.from("naveen"))
    return Buffer.from(str).toString ('base64');
};

const header = {
    alg: 'HS256',
    typ: 'JWT',
};
const b64Header = toBase64 (header);
// const jwtB64Header = replaceSpecialChars(b64Header);
console.log ("the header is: ",b64Header); 