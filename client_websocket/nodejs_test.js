// // test1.js
// console.log("Hello, Node.js Compiler!");











// // test2.js
// console.log("Missing parenthesis"
// // Missing closing )













// // test3.js
// console.log(undefinedVariable);
// console.log("This won't run");











// // test4.js
// console.log("Enter your name:");
// process.stdin.once('data', (data) => {
//     const name = data.toString().trim();
//     console.log(`Hello, ${name}!`);
//     process.exit();
// });












// // test5.js
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// rl.question('What is your age? ', (age) => {
//     console.log(`You are ${age} years old.`);
//     rl.close();
// });



// // test6.js
// console.log("Start");
// setTimeout(() => {
//     console.log("Timeout executed");
// }, 1000);
// console.log("End");








// // test7.js
// const fs = require('fs');

// fs.readFile('nonexistent.txt', 'utf8', (err, data) => {
//     if (err) {
//         console.error("File read error:", err.message);
//         return;
//     }
//     console.log("File content:", data);
// });




// // test7_success.js
// const fs = require('fs');
// fs.readFile('/mnt/c/Users/HP/Desktop/sais-project/online-compiler-v2/main.py', 'utf8', (err, data) => {
//     if (err) throw err;
//     console.log("File content:", data);
// });











// // test8.js
// const missing = require('./nonexistent-module');
// console.log(missing);




// // test8_valid.js
// const { add } = require('./math');
// console.log("5 + 3 =", add(5, 3));





// // test9.js
// async function testPromise() {
//     try {
//         await Promise.reject("Intentional failure");
//     } catch (err) {
//         console.log("Caught:", err);
//     }
// }
// testPromise();
// console.log("Async test running...");







// // test10.js
// const EventEmitter = require('events');
// const emitter = new EventEmitter();

// emitter.on('greet', (name) => {
//     console.log(`Hello, ${name}!`);
// });

// console.log("Emitting event...");
// emitter.emit('greet', 'Node.js');






// // test11.js
// const num = 42;
// num.toUpperCase();








// // test12.js
// setImmediate(() => {
//     throw new Error("Uncaught async error");
// });








// let a = 1;
// const b = 2;
// var c = 3;
// {
//   let a = 10;
//   console.log(a, b, c); // 10 2 3
// }
// console.log(a, b, c); // 1 2 3







// function foo() { console.log(x); var x = 5; }
// foo();






// function counter() {
//   let n = 0;
//   return () => ++n;
// }
// const inc = counter();
// console.log(inc(), inc());








// ;(function() {
//   console.log('IIFE ran');
// })();






// const name = 'Ada';
// console.log(`Hello ${name.toUpperCase()}!`);










// const [x, y] = [10, 20];
// const {a, b} = {a:1, b:2};
// console.log(x+y, a*b);











// const arr = [1,2,3];
// console.log([...arr,4].join(','), Math.max(...arr));







// const obj = {user: {profile: {age: null}}};
// console.log(obj?.user?.profile?.age ?? 18);







// const a = [10,20,30];
// for(let i=0;i<a.length;i++) process.stdout.write(a[i]+' ');
// console.log();
// for(const v of a) process.stdout.write(v+' ');
// console.log();
// for(const k in {x:1,y:2}) process.stdout.write(k+' ');
// console.log();







// let i=0; while(i<2) { process.stdout.write(i++ +''); }
// console.log();
// i=0; do { process.stdout.write(i++ +''); } while(i<2);
// console.log();




// const day=2;
// switch(day){
//   case 1: console.log('Mon'); break;
//   case 2: console.log('Tue'); break;
//   default: console.log('?');
// }






// try { throw new Error('boom'); }
// catch(e){ console.log(e.message); }
// finally { console.log('done'); }






// function greet(name='guest'){ console.log('Hi',name); }
// greet(); greet('Bob');




// function sum(...nums){ return nums.reduce((a,b)=>a+b,0); }
// console.log(sum(1,2,3,4));






// const sq = x=>x*x;
// function cube(x){return x*x*x;}
// console.log(sq(3),cube(3));







// function f(){}
// f.meta='info';
// console.log(f.meta);








// const key='age';
// const o={name:'Sam',[key]:30};
// console.log(o.name, o.age);







// function Animal(){}
// Animal.prototype.speak=function(){return 'sound'};
// const dog=Object.create(Animal.prototype);
// console.log(dog.speak());




// class Point{
//   constructor(x,y){this.x=x;this.y=y;}
//   dist(){return Math.hypot(this.x,this.y);}
// }
// const p=new Point(3,4);
// console.log(p.dist());





// class Circle{
//   #r;
//   set radius(v){this.#r=v;}
//   get area(){return Math.PI*this.#r**2;}
// }
// const c=new Circle(); c.radius=2;
// console.log(c.area.toFixed(2));







// const a=[3,1,4,1,5];
// console.log(a.sort((x,y)=>x-y).join(','), a.filter(x=>x>3).join(','), a.map(x=>x*2).join(','));










// const buf=new Uint8Array([65,66,67]);
// console.log(Buffer.from(buf).toString());











// setTimeout(()=>console.log('cb'),5000);
// console.log('sync');







// Promise.resolve(42).then(v=>console.log(v));
// console.log('now');







// (async()=>{
//   const v=await Promise.resolve('awaited');
//   console.log(v);
// })();
// console.log('start');







// Promise.all([Promise.resolve(1),Promise.resolve(2)]).then(a=>console.log(a.join(',')));
// Promise.race([
//   new Promise(r=>setTimeout(()=>r('fast'),10)),
//   new Promise(r=>setTimeout(()=>r('slow'),100))
// ]).then(console.log);







// setTimeout(()=>console.log('macro'),0);
// Promise.resolve().then(()=>console.log('micro'));
// console.log('sync');







// const fs=require('fs');
// fs.writeFileSync('tmp.txt','data');
// console.log(fs.readFileSync('tmp.txt','utf8'));









// const fs=require('fs').promises;
// (async()=>{
//   await fs.writeFile('tmp.txt','async');
//   console.log(await fs.readFile('tmp.txt','utf8'));
// })();




// const path=require('path');
// console.log(path.join(__dirname,'a','b'));




// const {Readable}=require('stream');
// const r=Readable.from(['a','b','c']);
// r.on('data',d=>process.stdout.write(d));
// r.on('end',()=>console.log());





// const http=require('http');
// const server = http.createServer((req,res)=>{res.end('ok');});
// server.listen(0,()=>{
//   const {port}=server.address();
//   console.log('listening',port);
//   server.close();
// });








// const {exec}=require('child_process');
// exec('echo hello',(err,stdout)=>console.log(stdout.trim()));






// console.log('bad






// console.log(undefinedVar);







// null.toString();



// Array(-1);




// (async()=>{
//   try {
//     await Promise.any([Promise.reject(1), Promise.reject(2)]);
//   } catch(e) {
//     console.log(e.errors.join(','));
//   }
// })();





// process.stdout.write('What is your age? ');
// process.stdin.once('data', (d) => {
//   const age = d.toString().trim();
//   console.log(`You are ${age} years old.`);
//   process.exit(0);
// });






// const rl = require('readline').createInterface({
//   input: process.stdin,
//   output: process.stdout,
//   terminal: true
// });
// rl.question('What is your age? ', (a) => {
//   console.log(`You are ${a} years old.`);
//   rl.close();
// });









// const rl = require('readline').createInterface({
//   input: process.stdin,
//   output: process.stdout,
//   terminal: true
// });
// rl.question('Password: ', { hideEchoBack: true }, (p) => {
//   console.log(`You typed: ${p}`);
//   rl.close();
// });








// Promise.reject('fail');
// setTimeout(() => console.log('continues'), 100);









// // infinite-loop.js
// console.log("Starting infinite loop... (Ctrl+C or kill to stop)");

// let counter = 1;

// setInterval(() => {
//   const timestamp = new Date().toISOString();
// //   console.log(`[${timestamp}] Count: ${counter}`);
//   counter++;
// }, 1000);










