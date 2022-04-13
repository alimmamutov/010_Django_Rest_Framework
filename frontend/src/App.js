import React from 'react';
import axios from 'axios';
// import logo from './logo.svg';
import './App.css';
import MainMenu from './components/MainMenu.js';
import UserList from './components/User.js';
import Footer from './components/Footer.js';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'authors': []
        }
    }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                this.setState(
                            {
                               'users': users
                            }
                )
            }).catch(error => console.log(error))
    }

    render () {
        return (
            <div>
                <MainMenu />
                <UserList users={this.state.users} />
                <Footer />
            </div>
        )
    }
}

export default App;