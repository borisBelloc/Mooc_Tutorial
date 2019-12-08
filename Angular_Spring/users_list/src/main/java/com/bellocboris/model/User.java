package com.bellocboris.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "myuser")
public class User {
	/**
	 * user is reserved name, need to change the table name with @Table
	 */
     
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private long id;
    private final String name;
    private final String email;
	
    
 // standard constructors / setters / getters / toString	
    // Empty constructor needed by JPA
    public User() {
        this.name = "unknow";
        this.email = "unknow";
    }
    
	public User(String name, String email) {
	super();
	this.name = name;
	this.email = email;
	}
	
	public long getId() {
		return id;
	}
	public void setId(long id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public String getEmail() {
		return email;
	}
	
	@Override
	public String toString() {
		return "User [id=" + id + ", name=" + name + ", email=" + email + "]";
	}
     
    
    
}