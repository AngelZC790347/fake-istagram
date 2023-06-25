import avatarLogo from '/avatar.svg'
import './profile.css'
import Post from '../components/Post.jsx'
import { useState } from 'react'
const Profile=({usuario})=>{
	let cookie = parseInt(document.cookie.match(/\d$/g)[0])
	const  [user,setUser]= useState(usuario)
	console.log(usuario.followed)
	const  [isFollowed,setFollow] = useState(usuario.followers.some(id=>id==cookie))
	console.log(isFollowed)
	return(
		<div>
			<header>
				<div style={{display: "flex"}}>
		  			<div><img style={{maxHeight:"75px",borderRadius:"50%",border:"solid 0.5px #b3b3b5",boxDirection:"revert-layer",marginRight:"50px"}} src={avatarLogo}/></div>
		  			<div >
		  				<div style={{height:"30px"}}>
		  					<h2>{user.user_name}</h2>
		  					{
		  						cookie!=null && cookie!="" && cookie !== undefined && cookie!=user.user_id?
		  						 <>		  						 	
		  						 	<button onClick={(ev)=>{
		  						 		
		  						 		setFollow(!isFollowed)
		  						 		let tmpuser = {...user}
		  						 		if(isFollowed) tmpuser.followers.pop(cookie)
		  						 		else tmpuser.followers.push(cookie)
		  						 		setUser(tmpuser)
		  						 		fetch("./api/user",{method: isFollowed?'DELETE' : 'PUT',credentials:'include',headers:{'Content-Type': 'application/json'},body:JSON.stringify(user)})
		  						 	}	
		  							} className={isFollowed?"followButton":""} >{isFollowed? "Dejar de Seguir":"Seguir"}</button>
		  							<button><a style={{textDecoration:"none"}} href="/auth/logout">Enviar Mensaje</a></button>
		  						</>
		  						:<><button>Editar Perfil</button>
		  						<button onClick={()=>document.cookie = "user_id=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;"}><a style={{textDecoration:"none"}} href="/auth/logout">Salir</a></button></>
		  					}	
		  				</div>
		  				<div style={{justifyContent: "space-between"}}>
			  				<span >{user.posts.length} publicaciones</span>
			  				<span>{user.followers.length} segidores</span>
			  				<span>{user.followed.length} seguidos</span>
		  				</div>
		  				<div style={{paddingTop:"10px"}}>
			  				<span >{user.email}</span>
		  				</div>
					</div>
				</div>	
			</header>
			<main>
				{
				}		 	
				{usuario.posts.length <= 0 ?<h3>No hay contenido aun</h3>: usuario.posts.map(post=><Post post={post}/> ) }
			</main>
		</div>
	)
}
export default Profile;