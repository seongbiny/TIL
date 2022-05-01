# Next.js

```
npm run dev
```

```javascript
export const getServerSideProps = async()=>{
    const res = await fetch('url');
    const posts = await res.json();
    
    return {
        props: {
            posts
        }
    }
}
```



