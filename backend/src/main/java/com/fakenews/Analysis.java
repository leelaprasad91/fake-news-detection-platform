package com.fakenews;
import jakarta.persistence.*; import java.time.Instant;
@Entity @Table(name="news_analysis")
public class Analysis {
 @Id @GeneratedValue(strategy=GenerationType.IDENTITY) private Long id;
 @Column(nullable=false,length=20000) private String newsText;
 @Column(nullable=false) private String prediction;
 private double confidence;
 private Instant createdAt=Instant.now();
 protected Analysis(){}
 public Analysis(String t,String p,double c){newsText=t;prediction=p;confidence=c;createdAt=Instant.now();}
 public Long getId(){return id;} public String getNewsText(){return newsText;} public String getPrediction(){return prediction;} public double getConfidence(){return confidence;} public Instant getCreatedAt(){return createdAt;}
}
