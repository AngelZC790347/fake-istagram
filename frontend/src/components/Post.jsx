import { useState } from 'react'
import './post.css'

const Post = ({post})=>{
	const [isVisible,setVisible] = useState(false)
	return(

		<div id='pst-container'  onClick={()=>showModal()}>
			<img onMouseOut={()=>{setVisible(false)}} onMouseEnter={()=>{setVisible(true)}} className='post_img'  src={post.photo} alt="" height={300}/>
			<spam className='info' style={{color:"white",position:"absolute",top:"12%" , left:"60px" ,display:isVisible?"inline":"none"}}>🤍 {post.likes} <br/>💬 {post.comments.length}</spam>
		</div>
	)
}

export default Post;