async function run(){

    const image = tf.browser.fromPixels(imager);
    const resized_image = 
         tf.image.resizeBilinear(image, [150,150]).toFloat();
    const offset = tf.scalar(255.0);
    const normalized = tf.scalar(1.0).sub(resized_image.div(offset));
    const batchedImage = normalized.expandDims(0);
    const MODEL_URL = 'http://02e2bb42.ngrok.io/model.json';
    const model = await tf.loadLayersModel(MODEL_URL);
    const result = model.predict(batchedImage);
    result.print();
    input = document.getElementById("result");
    input.value = result;
  }
  
  run();