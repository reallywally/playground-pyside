package com.wally.msa.product.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.math.BigDecimal;

@Document(value = "products")
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Getter
public class Product {
    @Id
    private String id;
    private String name;
    private String description;
    private BigDecimal price;
}
