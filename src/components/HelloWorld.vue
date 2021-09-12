hoge.vue
<template>
  <div id="search-ip">
    <div>
      <div>
        <input @click="getFolder" type="button" value="ファイルを取得">
      </div>
    </div>
  </div>
</template>

<script>  
  const archiver = require('archiver');
  import { PassThrough } from 'stream';

  var AWS = require('aws-sdk');
  AWS.config.update(
    {
      accessKeyId: "AKIAQ7J3FIK6FGBSTY7Q",
      secretAccessKey: "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",
    }
  );
  var s3 = new AWS.S3();

  const bucket_name = "tsugitasu-static"
  var files = [
    '/media/images/login_pic.2ee7e652.png',
    '/media/images/login_pic.2ee7e652.png',
  ]

  export default {
    name: 'SearchIp',
    methods: {
      getFolder() {
        const archive = archiver('zip', { zlib: { level: 5 } });
        
        for (let i = 0; i < files.length; i += 1) {
          const passthrough = new PassThrough();
          s3.getObject({
            Bucket: bucket_name,
            Key: files[i]
          })
          .createReadStream()
          .pipe(passthrough);
          archive.append(passthrough, { name: "file"+i+".png"});
        }
         archive.finalize();
      },

      getFile() {
        s3.getObject(
          { 
            Bucket: bucket_name, 
            Key: "media/images/login_pic.2ee7e652.png" 
          },
          function (error, data) {
            if (error != null) {
              alert("Failed to retrieve an object: " + error);
            } else {
              const blob = new Blob([data.Body], {type: data.ContentType});
              const fileURL = window.URL.createObjectURL(blob);
              const link = document.createElement('a')
              link.href = fileURL
              link.download = "login_pic.2ee7e652.png"
              link.click()
              document.body.removeChild(link);
            }
          }
        );
      }
    }
  }
</script>