import React from 'react';
import Icon from 'react-geomicons'
import { Flex, Box } from 'reflexbox';
import {
    Card,
    CardImage,
    Close,
    Container,
    Heading,
    Input,
    Message,
    Space } from 'rebass';

import MD5 from 'crypto-js/md5';


export default React.createClass({
    displayName: 'App',

    description: 'A pretty-doge-icon is a avatar which represents a hash of unique information.',

    getInitialState: function() {
        let initHash = MD5('Enter text here');
        return {
            imageURI: 'https://jmatt.org/d/' + initHash
        };
    },

    handleChange: function(e) {
        let newHash = MD5(e.target.value);
        this.setState({
            imageURI: 'https://jmatt.org/d/' + newHash
        });
    },

    render: function() {
        return (
            <Container>
                <Heading level={1}>generate a pretty-doge-icon</Heading>
                <Input
                    name="doge_icon_example"
                    placeholder="Enter text here"
                    rounded
                    type="text"
                    onChange={this.handleChange} />
                <Flex align='center' justify='center' auto={true}>
                    <Card rounded width={256}>
                    <CardImage src={this.state.imageURI}/>
                    </Card>
                </Flex>
                <Message inverted rounded theme="warning">
                    <Icon name='warning' />
                    {' Don\'t use sensitive information as text, your identicon could reveal it.'}
                    <Space auto x={1} />
                    <Close />
                </Message>
            </Container>
            

        );
    }
});