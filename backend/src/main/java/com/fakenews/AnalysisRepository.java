package com.fakenews;
import org.springframework.data.jpa.repository.JpaRepository; import java.util.List;
public interface AnalysisRepository extends JpaRepository<Analysis,Long>{List<Analysis> findTop20ByOrderByCreatedAtDesc();}
