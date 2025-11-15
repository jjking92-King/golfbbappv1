"""
Test suite for Golf Battle-Buddy Flask application.

This module contains unit and integration tests for the Flask web application,
testing routes, template rendering, and overall functionality.
"""

import pytest
from app import app


@pytest.fixture
def client():
    """
    Create a test client for the Flask application.
    
    This fixture provides a test client that can be used to make
    requests to the application without running a live server.
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def runner():
    """
    Create a test CLI runner for the Flask application.
    
    This fixture provides a runner that can invoke CLI commands
    registered with the Flask application.
    """
    return app.test_cli_runner()


class TestRoutes:
    """Test cases for application routes."""
    
    def test_index_route_exists(self, client):
        """Test that the index route (/) exists and returns 200 OK."""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_index_returns_html(self, client):
        """Test that the index route returns HTML content."""
        response = client.get('/')
        assert response.content_type == 'text/html; charset=utf-8'
    
    def test_index_contains_title(self, client):
        """Test that the index page contains the application title."""
        response = client.get('/')
        assert b'Golf Battle-Buddy' in response.data
    
    def test_404_for_invalid_route(self, client):
        """Test that invalid routes return 404 Not Found."""
        response = client.get('/nonexistent-page')
        assert response.status_code == 404


class TestTemplateRendering:
    """Test cases for template rendering."""
    
    def test_template_renders_successfully(self, client):
        """Test that the main template renders without errors."""
        response = client.get('/')
        assert response.status_code == 200
        assert len(response.data) > 0
    
    def test_template_contains_navigation(self, client):
        """Test that the template includes navigation elements."""
        response = client.get('/')
        # Check for navigation-related content
        assert b'nav' in response.data.lower() or b'header' in response.data.lower()
    
    def test_template_contains_meta_viewport(self, client):
        """Test that the template includes responsive meta viewport tag."""
        response = client.get('/')
        assert b'viewport' in response.data
    
    def test_template_is_valid_html(self, client):
        """Test that the response contains basic HTML structure."""
        response = client.get('/')
        data = response.data
        assert b'<!DOCTYPE html>' in data
        assert b'<html' in data
        assert b'</html>' in data
        assert b'<head>' in data
        assert b'<body>' in data


class TestApplicationConfiguration:
    """Test cases for application configuration."""
    
    def test_app_exists(self):
        """Test that the Flask app instance exists."""
        assert app is not None
    
    def test_app_is_flask_instance(self):
        """Test that app is a Flask instance."""
        from flask import Flask
        assert isinstance(app, Flask)
    
    def test_testing_config(self, client):
        """Test that testing configuration is properly set."""
        assert app.config['TESTING'] is True


class TestContentPresence:
    """Test cases for specific content presence in the application."""
    
    def test_page_contains_golf_references(self, client):
        """Test that the page contains golf-related content."""
        response = client.get('/')
        data = response.data.lower()
        # Check for golf-related terms
        assert b'golf' in data or b'tee' in data
    
    def test_page_has_charset_utf8(self, client):
        """Test that the page uses UTF-8 encoding."""
        response = client.get('/')
        assert b'charset=UTF-8' in response.data or b'charset="UTF-8"' in response.data
    
    def test_page_has_styles(self, client):
        """Test that the page includes styling."""
        response = client.get('/')
        # Check for either inline styles or linked stylesheets
        assert b'<style>' in response.data or b'<link' in response.data


class TestHTTPMethods:
    """Test cases for HTTP methods."""
    
    def test_index_accepts_get(self, client):
        """Test that the index route accepts GET requests."""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_index_rejects_post(self, client):
        """Test that the index route rejects POST requests (if not configured)."""
        response = client.post('/')
        # Flask returns 405 Method Not Allowed for unsupported methods
        assert response.status_code == 405
    
    def test_index_rejects_put(self, client):
        """Test that the index route rejects PUT requests."""
        response = client.put('/')
        assert response.status_code == 405
    
    def test_index_rejects_delete(self, client):
        """Test that the index route rejects DELETE requests."""
        response = client.delete('/')
        assert response.status_code == 405


class TestResponseHeaders:
    """Test cases for HTTP response headers."""
    
    def test_response_has_content_type(self, client):
        """Test that responses include Content-Type header."""
        response = client.get('/')
        assert 'Content-Type' in response.headers
    
    def test_response_has_content_length(self, client):
        """Test that responses include Content-Length header."""
        response = client.get('/')
        assert 'Content-Length' in response.headers
        assert int(response.headers['Content-Length']) > 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
