var posts=["posts/undefined.html","posts/reading-summary-2026.html","posts/shakespeare-sonnet-18.html","posts/undefined.html","posts/zhongkao-physics-optics.html","posts/zhongkao-physics-thermal.html","posts/zhongkao-physics-video.html"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };