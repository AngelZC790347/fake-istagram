import Post from './components/Post';
import {usePosts} from './services/userService'

const Inicio = ()=>{
	const {posts } = usePosts()	
	return(

		<div id='content-left'>{posts!=null && posts!=undefined && posts.length>0?posts.map(p=><div style={{borderBottom:"solid 0.2px ",marginBottom:60}}><h3>{p.owner}</h3><Post post={p}/><p style={{fontSize:10,fontWeight:10}}>{p.description}</p></div>):null}</div>
	)
}
export default Inicio;