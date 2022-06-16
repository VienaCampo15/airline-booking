import React from 'react'
import Typography from '@mui/material/Typography'
import { AppBar, Avatar, Box, Button, Container, Toolbar } from '@mui/material'
import ConnectingAirportsRoundedIcon from '@mui/icons-material/ConnectingAirportsRounded';

const NavBar = () => {
  const sxbutton = { 'borderRadius':1,
                      'm':1, 'mr':-0.5,
                      'color': '#3C096C',
                      'bgcolor':'#ebedf0',
                      fontFamily: 'courier new',
                      '&:hover': {'bgcolor':'#446bc9'} };
  return ( <>
        <AppBar position="fixed" sx={{bgcolor:'#10002B', background:'linear-gradient(40deg, #284da8, #446bc9, #68419c, #7653a3)', boxShadow:'none'}}>
          <Container maxWidth="xl">
              <Toolbar disableGutters>
                <Box noWrap component="a" href="/" sx={{bgcolor: '#240046', display:'inline-flex', boxShadow:1, borderRadius:4, borderColor:'#E0AAFF' , p:0.5, ml:-1}}>
                  <Avatar sx={{bgcolor:'#446bc9', mr:1.5}}>
                    <ConnectingAirportsRoundedIcon fontSize='medium' sx={{color:'#ebedf0'}} />
                  </Avatar>
                  <Typography variant="h6"
                    sx={{
                      mr: 0.5,
                      mt: 0.5,
                      fontFamily: 'courier new',
                      fontWeight: 150,                    
                      color: '#ebedf0',
                      textDecoration: 'none',
                    }}>
                      Aerolinea Norte-Sur
                    </Typography>
                </Box>
                <Box sx={{display:'inline-flex', flexGrow:1}}></Box>
                <Box sx={{display:'inline-flex'}}>
                    <Button size='small' variant='contained' sx={sxbutton} href="/catalog"   >
                      Flights Search
                    </Button>
                </Box>
                <Box sx={{display:'inline-flex'}}>
                    <Button size='small' variant='contained' sx={sxbutton} href="/catalog/all"   >
                      All Flights
                    </Button>
                </Box>
                    
             </Toolbar>
          </Container>
        </AppBar>
        <Toolbar/>
        </>

  )
}

export default NavBar